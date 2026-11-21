![Apps-reForged](Apps-reForged.png)

# splitForged

A lightweight, non-destructive Python command-line utility that splits markdown documents into smaller files based on specified heading levels.

## Overview

splitForged is built for writers and designers who plan, organize, or publish in large Markdown files—rule glossaries, spell lists, adventure modules, or any long document that needs to be broken into tidy, reusable pieces.

Drop a single Markdown file into the `Input` folder, choose a heading level, and the script writes a new file (or an alphabetized set of files) into `Output`. Your original document is never altered or deleted. Nested sub-headings, tables, lists, code blocks, and images are preserved exactly as they appear in the source.

## Features

- **Folder-Based Workflow:** Automatically generates `Input` and `Output` folders. Drop a single Markdown file into the `Input` folder, press Enter, and let the app do the rest.
- **Customizable Splitting & Conversion:** Choose exactly which header level to split your document by (H1 through H6). You can also optionally convert the targeted split headers to a different level upon export (e.g., split by H3 but save the new files starting with H1), leaving all nested sub-headers completely intact.
- **Dual Export Modes:**
  - **Individual Files:** Creates a separate Markdown file for every single header.
  - **A-Z Grouping:** Compiles sections alphabetically into `A.md`, `B.md`, etc., based on the first letter of the header. It also neatly groups numbered headers into files like `1.md` and symbols into a `Misc.md` file. Missing alphabetical letters (A–Z) are auto-populated with placeholder text so a glossary stays complete.
- **Smart Naming & Formatting:** Automatically names the newly generated Markdown files using the text of the corresponding headings. Spaces in all generated filenames (including prefixes) are replaced with underscores (`_`). Leading and trailing Markdown formatting characters (asterisks `*`, underscores `_`, dashes `-`, tildes `~`, and backticks `` ` ``) are stripped from headers so filenames stay clean and readable.
- **Custom Prefixes:** Optionally add a custom prefix (like `Magic_Spells_`) to bulk-rename all exported files instantly.
- **Continuous Workflow:** The app loops, asking if you have another file to split, so you can process multiple documents in one session.
- **Visual Reporting:** Provides real-time console feedback as each file is created, plus a summary of the total sections processed at the end.
- **Input Validation:** Invalid header levels or export choices are rejected with a "try again" prompt rather than silently falling back to a default. Leaving a prompt blank still applies the documented default.
- **Non-Destructive & Clean:** Your original source file is never altered or deleted. Excess blank lines are trimmed so exported Markdown stays flush.
- **Organized Output:** All generated files are deposited into the `Output` folder to keep your working directory tidy.
- **Robust:** Handles large files and copies complex Markdown elements like tables, nested lists, code blocks, and images.

## Requirements

- Python 3.6+ installed on your system.
- No external libraries are required. The script uses only the Python standard library.

## Installation

1. **Download** the script to your local machine. You can clone the repository or download the latest release:

   ```
   git clone https://github.com/oldmanumby/splitForged.git
   cd splitForged
   ```

2. **Make it executable** (macOS/Linux only):

   ```
   chmod +x splitForged.py
   ```

## Usage

Place the script in a folder of your choice. On first run it creates `Input` and `Output` folders alongside the script. Drop **one** Markdown (`.md`) file into `Input`, then return to the terminal and follow the prompts.

### Running the Script

**macOS / Linux:**

```
./splitForged.py
# or
python3 splitForged.py
```

**Windows:**

```
python splitForged.py
```

### Interactive Prompts

1. Press `Enter` to confirm the file is in place.
2. **Header Level:** Enter the level you want to split by (e.g., `H1`, `H2`, `H3`). Pressing `Enter` without typing anything defaults to `H1`.
3. **Target Header Level:** Enter the new level you want the split headers converted to (e.g., `H1`), or press `Enter` to leave them as they are. This only changes the headers where the split occurs, not nested headers.
4. **Export Type:** Choose `1` for Individual files or `2` for an alphabetized A–Z export.
5. **Prefix:** Add a prefix for the exported files, or press `Enter` to skip.
6. **Continue:** When the split is complete, remove the old file from the `Input` folder, place a new one, and type `y` to process another document, or `n` to quit.

### Sample Prompts

```
Welcome to splitForged v1.12.1 by Old Man Umby!

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
  ...
  -> Created: Output/Glossary_Z.md
  -> Created: Output/Glossary_Misc.md

Splitting complete!
Total sections processed: 87

Do you want to process another file? (y/n):
> n

Exiting splitForged. Goodbye!
```

### Example Workflow

1. **Prepare your document:** Make sure the Markdown file uses consistent heading levels at the points where you want to split.
2. **Run the script:** Launch splitForged and drop the file into `Input`.
3. **Choose split and export options:** Pick a heading level, an optional converted heading level, Individual or A–Z export, and an optional filename prefix.
4. **Check your output:** Review the files in `Output`, then process another document or quit.

## Advanced Features

- **Header Level Conversion:** Changing the output heading level rewrites only the heading that starts each split section. Nested headings keep their original level.
- **A–Z Grouping Details:** Grouping looks at the first alphanumeric character in the heading, so styled headings (for example `**Bold Title**`) still sort under `B` instead of `Misc`. Empty placeholder files are created only for missing letters A–Z, with the text `There is no content for this letter.` Numbered files (`0.md`–`9.md`) and `Misc.md` are created only when matching headings exist.
- **Filename Sanitization:** Invalid filename characters (`\ / * ? : " < > |`) are removed. If a heading is nothing but formatting symbols, the file is named `Untitled_Section_N.md`.
- **Existing Output Files:** Files in `Output` with the same name are overwritten. Clear or rename previous exports if you need to keep them.

## Troubleshooting

- **No markdown (.md) files found in the Input folder:** Place exactly one `.md` file in `Input` and try again. The script ignores non-Markdown files.
- **Multiple markdown files found:** splitForged processes one document at a time. Leave only a single `.md` file in `Input`.
- **No Hn headers found:** Confirm the document actually uses ATX headings at the level you selected (for example `## Heading` for H2), at the start of the line.
- **Invalid header level or export type:** Enter `H1` through `H6`, or `1` / `2` for the export type. Blank input is accepted only where a default is documented.
- **Unexpected filenames:** Emphasis and other wrapping Markdown on a heading is stripped before the filename is built. If a name still looks wrong, check the source heading text.

## License

This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**.

You are free to use, modify, and distribute this software, provided that you:

- Disclose the source code of any modifications you make.
- License your modified versions under the same GPL-3.0 license.
- Preserve the original copyright notices and disclaimers.

See the [LICENSE](LICENSE.md) file for the complete text of the GPL-3.0 license.
