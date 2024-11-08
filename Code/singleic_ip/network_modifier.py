import sys
import os

# Function to remove extra spaces after tabs in a line
def remove_space_after_tab(line):
    parts = line.split("\t")
    if len(parts) > 1:
        parts[1] = parts[1].strip()  # Remove trailing whitespace
        return "\t".join(parts)
    else:
        return line

# Function to get the directory of an additional file named "external.txt"
def get_directory_of_extra_file(input_file):
    # Get the directory of the input file
    file_directory = os.path.dirname(os.path.abspath(input_file))

    # Construct the path of the additional file
    extra_file_path = os.path.join(file_directory, "external.txt")

    # Check if the additional file exists
    if os.path.isfile(extra_file_path):
        return extra_file_path
    else:
        return "nothing"    # Indicate that the additional file does not exist

# Function to modify the network rules in the input file and create a new file with modified rules
def network_modifier(input_file):
    # Read the input file
    with open(input_file, 'r') as f:
        lines = f.readlines()
        first_line = lines[0].strip()  # Get the first line of the file

    # Get the path of the additional gene network file
    ext = get_directory_of_extra_file(input_file)

    # If the additional file exists
    if ext != "nothing":
        with open(ext, 'r') as f:
            ext_lines = f.readlines()   # Read lines from the additional file

    # Write modified network rules to a new file named "allowed_file.txt"
    with open('allowed_file.txt', 'w') as f:
        # Write header for the new file
        f.write("Gene\tRule\n")

        if first_line.startswith("Gene"):
            # Iterate through lines in the input file, excluding the header
            for line in lines[1:]:
                words = line.split()

                # Check if '_' in gene name, and if so, combine them
                gene_name = words[0]
                if '_' in gene_name:
                    gene_name = gene_name.replace('_', '')

                # Modify the line by removing '=' and replacing 'AND', 'OR', 'NOT'
                modified_line = gene_name + '\t' + ' '.join(words[1:]).replace('=', '')

                if 'AND' in modified_line:
                    modified_line = modified_line.replace('AND', 'and')
                if 'OR' in modified_line:
                    modified_line = modified_line.replace('OR', 'or')
                if 'NOT' in modified_line:
                    modified_line = modified_line.replace('NOT', 'not')

                modified_line = remove_space_after_tab(modified_line)

                # Write the modified line to the new file
                f.write(modified_line + '\n')

            # If the additional file exists
            if ext != "nothing":
                for gene in ext_lines:
                    words = gene.split()

                    # Check if '_' in gene name, and if so, combine them
                    gene_name = words[0]
                    if '_' in gene_name:
                        gene_name = gene_name.replace('_', '')

                    # Create a new line by enclosing the gene name in parentheses
                    extra_gene = gene_name + '\t' + '( ' + gene_name + ' )'
                    f.write(extra_gene + '\n')

        # If the first line does not start with "Gene"
        else:
            for line in lines:
                words = line.split()

                # Check if '_' in gene name, and if so, combine them
                gene_name = words[0]
                if '_' in gene_name:
                    gene_name = gene_name.replace('_', '')

                # Modify the line by removing '=' and replacing 'AND', 'OR', 'NOT'
                modified_line = gene_name + '\t' + ' '.join(words[1:]).replace('=', '')

                if 'AND' in modified_line:
                    modified_line = modified_line.replace('AND', 'and')
                if 'OR' in modified_line:
                    modified_line = modified_line.replace('OR', 'or')
                if 'NOT' in modified_line:
                    modified_line = modified_line.replace('NOT', 'not')
                modified_line = remove_space_after_tab(modified_line)

                # Write the modified line to the new file
                f.write(modified_line + '\n')

            if ext != "nothing":
                for gene in ext_lines:
                    words = gene.split()

                    # Check if '_' in gene name, and if so, combine them
                    gene_name = words[0]
                    if '_' in gene_name:
                        gene_name = gene_name.replace('_', '')

                    # Create a new line by enclosing the gene name in parentheses
                    extra_gene = gene_name + '\t' + '( ' + gene_name + ' )'
                    f.write(extra_gene + '\n')

    # Return the path of the new file
    return 'allowed_file.txt'

input_file = sys.argv[1]

# Call the network_modifier function to modify the network rules in the input file
modified_file = network_modifier(input_file)

# Print the path of the modified file
print(modified_file)

