import nbformat

def add_remove_cell_tag(notebook_path):
    try:
        # Load the notebook
        with open(notebook_path, "r", encoding="utf-8") as f:
            notebook = nbformat.read(f, as_version=4)

        # Iterate through the cells
        for cell in notebook.cells:
            # Check if the cell is a code cell with '#exclude' or a markdown cell with '<!-- exclude -->'
            if (cell.cell_type == "code" and "#exclude" in cell.source) or \
               (cell.cell_type == "markdown" and "<!-- exclude -->" in cell.source):
                # Add 'remove-cell' tag to the metadata
                tags = cell.metadata.get("tags", [])
                if "remove-cell" not in tags:
                    tags.append("remove-cell")
                cell.metadata["tags"] = tags

        # Save the updated notebook
        with open(notebook_path, "w", encoding="utf-8") as f:
            nbformat.write(notebook, f)

        print(f"Updated notebook saved: {notebook_path}")

    except Exception as e:
        print(f"Error processing notebook: {e}")

# Example usage
notebook_path = "final.ipynb"
add_remove_cell_tag(notebook_path)