# markdown-index-autogen
Automatically generate / refresh markdown index with updated folder structure

## Summary
This tool is used for maintain a list of reading materials (papers) with auto-generated indexes in markdown format.
I can't find one available so make one by myself.

An example of running this tool: (python3)
```
python autogen.py -e .txt
```

## Generated index
[comment]: # (markdown-index-autogen)

Below content will remain unchanged.

## As pre-commit hook
.pre-commit-config.yaml:
```
repos:
- repo: https://github.com/ksang/markdown-index-autogen
  rev: v0.1.0
  hooks:
  - id: markdown-index-autogen
    args: ["-e .txt"]
```