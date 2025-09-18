import nbformat

def remove_hide_input_tag_for_op(notebook_path):
    try:
        # Load the notebook
        with open(notebook_path, "r", encoding="utf-8") as f:
            notebook = nbformat.read(f, as_version=4)

        # Iterate through the cells
        for cell in notebook.cells:
            if cell.cell_type == "code" and "#op" in cell.source:
                # Check if the 'hide-input' tag is present and remove it
                if "tags" in cell.metadata:
                    cell.metadata["tags"] = [
                        tag for tag in cell.metadata["tags"] if tag != "hide-input"
                    ]

        # Save the updated notebook
        with open(notebook_path, "w", encoding="utf-8") as f:
            nbformat.write(notebook, f)

        print(f"'hide-input' tag removed for cells with #op in notebook: {notebook_path}")

    except Exception as e:
        print(f"Error processing notebook: {e}")

# Example usage
notebook_path = "final.ipynb"  # Replace with your notebook path
remove_hide_input_tag_for_op(notebook_path)