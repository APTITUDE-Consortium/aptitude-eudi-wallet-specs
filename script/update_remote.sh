#!/usr/bin/env sh

set -eu

script_dir="$(cd "$(dirname "$0")" && pwd)"
repo_root="$(cd "$script_dir/.." && pwd)"

cd "$repo_root"

submodule_list_file="$(mktemp)"
dirty_submodules_file="$(mktemp)"

cleanup() {
	rm -f "$submodule_list_file" "$dirty_submodules_file"
}

trap cleanup EXIT INT TERM

get_default_branch() {
	submodule_path="$1"

	git -C "$submodule_path" remote set-head origin -a >/dev/null 2>&1 || true
	head_ref="$(git -C "$submodule_path" symbolic-ref --quiet --short refs/remotes/origin/HEAD 2>/dev/null || true)"

	if [ -n "$head_ref" ]; then
		printf '%s\n' "${head_ref#origin/}"
		return 0
	fi

	printf '%s\n' "main"
}

echo "Synchronizing submodule configuration..."
git submodule sync --recursive
git submodule update --init --recursive

git config -f .gitmodules --get-regexp '^submodule\..*\.path$' > "$submodule_list_file"

while read -r key submodule_path; do
	if [ -n "$(git -C "$submodule_path" status --short)" ]; then
		printf '%s\n' "$submodule_path" >> "$dirty_submodules_file"
	fi
done < "$submodule_list_file"

if [ -s "$dirty_submodules_file" ]; then
	echo "Refusing to update dirty submodules:" >&2
	sed 's/^/  /' "$dirty_submodules_file" >&2
	echo "Commit, stash, or discard those changes before running this script again." >&2
	exit 1
fi

while read -r key submodule_path; do
	submodule_name="${key#submodule.}"
	submodule_name="${submodule_name%.path}"

	branch="$(git config -f .gitmodules --get "submodule.${submodule_name}.branch" || true)"

	echo "Fetching updates for ${submodule_path}..."
	git -C "$submodule_path" fetch --prune origin

	if [ -z "$branch" ]; then
		branch="$(get_default_branch "$submodule_path")"
	fi

	target_ref="origin/${branch}"

	if ! git -C "$submodule_path" rev-parse --verify --quiet "$target_ref" >/dev/null; then
		echo "Could not resolve ${target_ref} for ${submodule_path}." >&2
		exit 1
	fi

	current_commit="$(git -C "$submodule_path" rev-parse HEAD)"
	target_commit="$(git -C "$submodule_path" rev-parse "$target_ref")"

	if [ "$current_commit" = "$target_commit" ]; then
		echo "${submodule_path} is already at ${target_ref}."
		continue
	fi

	git -C "$submodule_path" checkout --detach "$target_commit" >/dev/null
	echo "Updated ${submodule_path} to ${target_ref} (${target_commit})."

	git -C "$submodule_path" submodule sync --recursive >/dev/null
	git -C "$submodule_path" submodule update --init --recursive >/dev/null
done < "$submodule_list_file"

echo "All linked submodules are now aligned with their latest remote commits."
