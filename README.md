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
   python3 splitPhorge.py
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

## Sample Prompts

```
Welcome to splitPhorge v1.12.1 by Old Man Umby!

Please place the file in the 'Input' folder and press [Enter/Return] to continue...

> [User presses Enter]

Found file: Rules_Glossary.md

Enter the header level to begin each split (H1-H6) [Default: H1]:
> H1

Would you like to convert the split headers to a different level while outputting?
Note: This ONLY changes the headers where the split occurs, not other nested headers.

Enter the new output header level for the split (H1-H6) [Default: Leave as is]:
> 

Export Options:

1. Export to Individual Files
2. Export to A-Z Files

Select export type (1 or 2):
> 2

Enter an optional filename prefix (e.g., 'Magic Spells - ') or press Enter to skip:
> Glossary_

Splitting file...
  -> Created: Output/Glossary_A.md
  -> Created: Output/Glossary_B.md
  -> Created: Output/Glossary_C.md
  -> Created: Output/Glossary_D.md
  -> Created: Output/Glossary_E.md
  -> Created: Output/Glossary_F.md
  -> Created: Output/Glossary_G.md
  -> Created: Output/Glossary_H.md
  -> Created: Output/Glossary_I.md
  -> Created: Output/Glossary_J.md
  -> Created: Output/Glossary_K.md
  -> Created: Output/Glossary_L.md
  -> Created: Output/Glossary_M.md
  -> Created: Output/Glossary_N.md
  -> Created: Output/Glossary_O.md
  -> Created: Output/Glossary_P.md
  -> Created: Output/Glossary_Q.md
  -> Created: Output/Glossary_R.md
  -> Created: Output/Glossary_S.md
  -> Created: Output/Glossary_T.md
  -> Created: Output/Glossary_U.md
  -> Created: Output/Glossary_V.md
  -> Created: Output/Glossary_W.md
  -> Created: Output/Glossary_X.md
  -> Created: Output/Glossary_Y.md
  -> Created: Output/Glossary_Z.md
  -> Created: Output/Glossary_Misc.md

Splitting complete!
Total sections processed: 87

Do you want to process another file? (y/n):
> n

Exiting splitPhorge. Goodbye!
```

## License

This project is open-source and available under the [GNU General Public License v3.0 (GPL-3.0)](LICENSE.txt).