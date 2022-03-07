# markdown-index-autogen
Automatically generate / refresh markdown index with updated folder structure

## Summary
This tool is used for maintain a list of reading materials (papers) with auto-generated indexes in markdown format.
I can't find one available so make one by myself.

An example of running this tool: (python3)
```
python gen.py -e .txt
```

## Generated index
[comment]: # (markdown-index-autogen)
- [example_folder_a](./example_folder_a)
	- [example_a_1.txt](./example_folder_a/example_a_1.txt)
- [example_folder_b](./example_folder_a/example_folder_b)
	- [example_b_1.txt](./example_folder_a/example_folder_b/example_b_1.txt)
- [example_folder_c](./example_folder_c)
	- [example_c_1.txt](./example_folder_c/example_c_1.txt)
	- [example_c_2.txt](./example_folder_c/example_c_2.txt)

Below content will remain unchanged.