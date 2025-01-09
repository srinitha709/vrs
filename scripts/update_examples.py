import os

def extract_examples(file_path):
    """Extract examples from source files."""
    examples = []
    with open(file_path, 'r') as f:
        for line in f:
            if line.strip().startswith(">>>"):
                examples.append(line.strip())
    return examples

def update_docs(doc_path, examples):
    """Insert updated examples into documentation."""
    print(f"Reading from: {doc_path}")  # Debugging output
    with open(doc_path, 'r') as f:
        content = f.readlines()

    updated_content = []
    inside_placeholder = False
    for line in content:
        if line.strip() == "# Examples will be dynamically updated here.":
            inside_placeholder = True
            updated_content.append(".. code-block:: python\n\n")
            for example in examples:
                updated_content.append(f"    {example}\n")
        elif inside_placeholder and line.strip() == "":
            inside_placeholder = False
        elif not inside_placeholder:
            updated_content.append(line)

    with open(doc_path, 'w') as f:
        f.writelines(updated_content)
    print(f"Updated {doc_path} with new examples.")  # Debugging output

# Example usage
source_file_path = 'examples/example.py'  # Path to the source code file
doc_file_path = 'docs/source/examples.rst'  # Path to the documentation file

print(f"Extracting examples from: {source_file_path}")  # Debugging output
examples = extract_examples(source_file_path)  # Pass the actual file path here
print(f"Extracted examples: {examples}")  # Debugging output

print(f"Updating documentation: {doc_file_path}")  # Debugging output
update_docs(doc_file_path, examples)
print("Documentation updated successfully!")  # Final success message
