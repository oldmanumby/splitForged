![Apps rePhorged](Apps_rePhorged.png)

# splitPhorge

A lightweight, non-destructive Python command-line utility that splits Markdown documents into smaller files based on specified heading levels.

## Features

- **Folder-Based Workflow:** Automatically generates `Input` and `Output` folders. Drop a single markdown file into the `Input` folder, press Enter, and let the app do the rest!
- **Customizable Splitting & Conversion:** Choose exactly which header level to split your document by (H1 through H6). You can also optionally convert the targeted split headers to a different level upon export (e.g., split by H3 but save the new files starting with H1), leaving all nested sub-headers completely intact.
- **Dual Export Modes:**
  - **Individual Files:** Creates a separate Markdown file for every single header.
  - **A-Z Grouping:** Compiles sections alphabetically into `A.md`, `B.md`, etc., based on the first letter of the header. It also neatly groups numbered headers into files like `1.md` and symbols into a `Misc.md` file. It will auto-populate missing alphabetical letters (A-Z) with placeholder text to ensure your glossary is complete!
- **Smart Naming & Formatting:** Automatically names the newly generated Markdown files using the text of the corresponding headings. Spaces in all generated filenames (including prefixes) are automatically replaced with underscores (`_`). Furthermore, the app automatically strips leading and trailing markdown formatting characters (such as asterisks `*`, underscores `_`, dashes `-`, tildes `~`, and backticks ```) from the headers to guarantee perfectly clean, readable filenames.
- **Custom Prefixes:** Optionally add a custom prefix (like `Magic_Spells_`) to bulk-rename all exported files instantly.
- **Continuous Workflow:** The app loops, asking if you have another file to split, so you can process multiple documents in one session.
- **Visual Reporting:** Provides real-time console feedback as each file is created, plus a summary of the total sections processed at the end.
- **Non-Destructive & Clean:** Your original source file is never altered or deleted. The app also strictly trims excess blank lines to ensure your exported Markdown formatting is perfectly flush.
- **Organized Output:** Automatically deposits all generated files into the clean `Output` folder to keep your working directory tidy.
- **Robust:** Easily handles large files and seamlessly copies complex Markdown elements like tables, nested lists, code blocks, and images.

## Prerequisites

- Python 3.x installed on your system. No external libraries are required.

## Usage

1. Place the `splitPhorge.py` script in a folder of your choice and run it using Python:

   ```
   python splitPhorge.py
   ```

2. The app will automatically generate two folders alongside it: `Input` and `Output`.

3. Drop the **single Markdown file** you wish to split into the `Input` folder.

4. Return to your terminal and follow the interactive prompts:

   - Press `Enter` to confirm the file is in place.
   - **Header Level:** Enter the level you want to split by (e.g., `H1`, `H2`, `H3`). Pressing `Enter` without typing anything will automatically default to `H1`.
   - **Target Header Level:** Enter the new level you want the split headers to be converted to (e.g., `H1`), or press `Enter` to leave them as they are.
   - **Export Type:** Choose `1` for Individual files or `2` for an alphabetized A-Z export.
   - **Prefix:** Add a prefix for the exported files or press `Enter` to skip.
   - **Continue:** When the split is complete, remove the old file from the `Input` folder, place a new one, and type `y` to process another document, or `n` to quit.

## License

This project is open-source and available under the [GNU General Public License v3.0 (GPL-3.0)](LICENSE.txt).