# splitPhorge v1.10
# Updates: Changed folder names from Process/Exports to Input/Output.

import os
import re
import string

def main():
    process_dir = "Input"
    export_dir = "Output"

    # Ensure the root folders exist when the app starts
    os.makedirs(process_dir, exist_ok=True)
    os.makedirs(export_dir, exist_ok=True)

    while True:
        print("\n--- splitPhorge ---")
        
        input(f"Please place the file in the {process_dir} folder and hit [Enter/Return] to continue...")

        # Scan the Input folder for markdown files
        md_files = [f for f in os.listdir(process_dir) if f.lower().endswith('.md')]

        if len(md_files) == 0:
            print(f"Error: No markdown (.md) files found in the '{process_dir}' folder.")
            if input("Do you want to try again? (y/n): ").strip().lower() != 'y':
                break
            continue
        elif len(md_files) > 1:
            print(f"Error: Multiple markdown files found in the '{process_dir}' folder.")
            print("Please ensure only ONE file is placed in the folder to process.")
            if input("Do you want to try again? (y/n): ").strip().lower() != 'y':
                break
            continue

        filename = os.path.join(process_dir, md_files[0])
        print(f"\nFound file: {md_files[0]}")

        header_input = input("Enter the header level to split by (H1-H6) [Default: H1]: ").strip().upper()
        if not header_input:
            header_input = "H1"
        
        if header_input not in [f"H{i}" for i in range(1, 7)]:
            print("Invalid header level. Defaulting to H1.")
            header_input = "H1"

        print("\n(Note: You can optionally convert the split headers to a different level.")
        print(" This ONLY changes the headers where the split occurs, not nested headers.)")
        target_header_input = input("Enter the target header level for the split (H1-H6) [Default: Leave as is]: ").strip().upper()
        
        target_header_level = None
        if target_header_input in [f"H{i}" for i in range(1, 7)]:
            target_header_level = int(target_header_input[1])
        elif target_header_input:
            print("Invalid target level. Leaving headers as is.")

        print("\nExport Options:")
        print("1. Export to Individual Files")
        print("2. Export to A-Z Files")
        export_type = input("Select export type (1 or 2): ").strip()
        if export_type not in ['1', '2']:
            print("Invalid option. Defaulting to 1 (Individual Files).")
            export_type = '1'

        file_prefix = input("Enter an optional filename prefix (e.g., 'Magic Spells - ') or press Enter to skip: ")

        # Determine the prefix string (e.g., "### " for H3)
        header_level = int(header_input[1])
        prefix_str = '#' * header_level + ' '
        
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()

            # Regex to find the exact start of the specified headers
            pattern = r'(?m)^' + re.escape(prefix_str) + r'(.*)'
            matches = list(re.finditer(pattern, content))

            if not matches:
                print(f"No {header_input} headers found in {md_files[0]}.")
            else:
                chunks = []
                for i, match in enumerate(matches):
                    start = match.start()
                    end = matches[i+1].start() if i + 1 < len(matches) else len(content)
                    
                    chunk_text_raw = content[start:end]
                    
                    if target_header_level:
                        target_prefix_str = '#' * target_header_level + ' '
                        if chunk_text_raw.startswith(prefix_str):
                            chunk_text_raw = target_prefix_str + chunk_text_raw[len(prefix_str):]

                    # The FIX: .strip() removes all leading/trailing extra blank lines from the chunk
                    chunk_text = chunk_text_raw.strip()
                    header_text = match.group(1).strip()
                    
                    # Strip leading and trailing markdown formatting (*, _, -, ~, `) for clean filenames
                    header_text = re.sub(r'^[*_\-~`\s]+|[*_\-~`\s]+$', '', header_text)
                    
                    # Fallback if the header is just empty symbols
                    if not header_text:
                        header_text = f"Untitled_Section_{i+1}"
                        
                    chunks.append((header_text, chunk_text))

                print("\nSplitting file...")

                if export_type == '1':
                    for header_text, chunk_text in chunks:
                        # Clean filename characters
                        safe_filename = re.sub(r'[\\/*?:"<>|]', "", header_text)
                        # Replace spaces with underscores
                        out_name = f"{file_prefix}{safe_filename}".replace(" ", "_") + ".md"
                        out_path = os.path.join(export_dir, out_name)
                        
                        with open(out_path, 'w', encoding='utf-8') as out_f:
                            # Write text with exactly one trailing newline
                            out_f.write(chunk_text + '\n')
                        
                        # Print the created file path
                        print(f"  -> Created: {out_path.replace(os.sep, '/')}")
                            
                elif export_type == '2':
                    # Setup A-Z, 0-9, and Misc groups
                    groups = {char: [] for char in string.ascii_uppercase}
                    for i in range(10):
                        groups[str(i)] = []
                    groups['Misc'] = []

                    for header_text, chunk_text in chunks:
                        # Find the true first alphanumeric character for sorting, bypassing ** or _
                        match_char = re.search(r'[A-Za-z0-9]', header_text)
                        first_char = match_char.group(0).upper() if match_char else 'Misc'
                        
                        if first_char in groups:
                            groups[first_char].append(chunk_text)
                        else:
                            groups['Misc'].append(chunk_text)

                    for key, texts in groups.items():
                        # Skip empty content for numbers and 'Misc'
                        if not texts and key not in string.ascii_uppercase:
                            continue

                        # Replace spaces with underscores
                        out_name = f"{file_prefix}{key}".replace(" ", "_") + ".md"
                        out_path = os.path.join(export_dir, out_name)
                        
                        with open(out_path, 'w', encoding='utf-8') as out_f:
                            if not texts:
                                out_f.write("There is no content for this letter.\n")
                            else:
                                # Join grouped chunks with exactly ONE blank line between them (\n\n)
                                out_f.write('\n\n'.join(texts) + '\n')
                                
                        # Print the created file path
                        print(f"  -> Created: {out_path.replace(os.sep, '/')}")
                                
                print("\nSplitting complete!")
                print(f"Total sections processed: {len(chunks)}")

        except Exception as e:
            print(f"An error occurred: {e}")

        if input("\nDo you have another file to split? (y/n): ").strip().lower() != 'y':
            print("Exiting splitPhorge. Goodbye!")
            break

if __name__ == "__main__":
    main()