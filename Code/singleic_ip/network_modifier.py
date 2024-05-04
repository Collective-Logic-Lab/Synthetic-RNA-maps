import sys
import os

def remove_space_after_tab(line):
    parts = line.split("\t")
    if len(parts) > 1:
        parts[1] = parts[1].strip()
        return "\t".join(parts)
    else:
        return line

def get_directory_of_extra_file(input_file):

    file_directory = os.path.dirname(os.path.abspath(input_file))

    extra_file_path = os.path.join(file_directory, "external.txt")
    if os.path.isfile(extra_file_path):
        return extra_file_path
    else:
        return "nothing"

def network_modifier(input_file):

    with open(input_file, 'r') as f:
        lines = f.readlines()
        first_line = lines[0].strip()

    ext = get_directory_of_extra_file(input_file)
    
    if ext != "nothing":
        with open(ext, 'r') as f:
            ext_lines = f.readlines()
    
    with open('allowed_file.txt', 'w') as f:
        
        f.write("Gene\tRule\n")
        
        if first_line.startswith("Gene"):
            
            for line in lines[1:]:

                words = line.split()          
    
                modified_line = words[0] + '\t' + ' '.join(words[1:]).replace('=','')

                if 'AND' in modified_line:
                    modified_line = modified_line.replace('AND', 'and')
                if 'OR' in modified_line:
                    modified_line = modified_line.replace('OR', 'or')
                if 'NOT' in modified_line:
                    modified_line = modified_line.replace('NOT', 'not')
                modified_line = remove_space_after_tab(modified_line)

                f.write(modified_line + '\n')
            
            if ext != "nothing":
                for gene in ext_lines:

                    words = gene.split()

                    extra_gene = words[0] + '\t' + '( ' + words[0] + ' )'
                    f.write(extra_gene + '\n')

        else:

            for line in lines:
    
                words = line.split()

                modified_line = words[0] + '\t' + ' '.join(words[1:]).replace('=','')

                if 'AND' in modified_line:
                    modified_line = modified_line.replace('AND', 'and')
                if 'OR' in modified_line:
                    modified_line = modified_line.replace('OR', 'or')
                if 'NOT' in modified_line:
                    modified_line = modified_line.replace('NOT', 'not')
                modified_line = remove_space_after_tab(modified_line)

                f.write(modified_line + '\n')
            
            if ext != "nothing":
                for gene in ext_lines:
          
                    words = gene.split()
  
                    extra_gene = words[0] + '\t' + '( ' + words[0] + ' )'
                    f.write(extra_gene + '\n')

    return 'allowed_file.txt'

input_file = sys.argv[1]
modified_file = network_modifier(input_file)
print(modified_file)
