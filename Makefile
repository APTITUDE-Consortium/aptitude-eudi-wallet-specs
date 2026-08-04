.PHONY: lint

lint:
	npx --yes markdownlint-cli --config .markdownlint.json --ignore-path .markdownlintignore 'docs/**/*.md'
