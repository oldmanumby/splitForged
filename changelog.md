# splitPhorge Changelog

All notable changes to this project will be documented in this file.

## [v1.12.1]

### Changed

- **License Update:** Transitioned the project license from MIT to the GNU General Public License v3.0 (GPL-3.0). Updated the script metadata and README to reflect this change.

## [v1.12.0]

### Added

- **Metadata Header:** Integrated a standardized Python metadata block at the top of the script (including author, copyright, license, version, etc.) to formalize project tracking.
- **Dynamic Versioning:** The welcome message now dynamically pulls the version number directly from the `__version__` metadata variable.

## [v1.11]

### Added

- **UI Uniformity & Welcome Message:** Added a "Welcome to splitPhorge" banner displaying the current version and author at startup. Improved general readability by adding line breaks and a `> `prompt indicator for all interactive user questions.
- **Input Validation Loops:** Replaced silent default fallbacks with strict input validation. The app now requires users to enter a valid option (or explicitly leave blank for the default) for header levels and export types, prompting them to "try again" if an invalid entry is detected.
- **End Prompt Clarification:** Updated the final loop prompt to ask "Do you want to process another file?" for clearer workflow semantics.

## [v1.10]

### Changed

- **Folder Renaming:** Renamed the root directories from `Process` to `Input` and `Exports` to `Output` for clearer semantics.

## [v1.9]

### Changed

- **Folder-Based Workflow:** Replaced the filename typing prompt with a streamlined, folder-based approach. The app now automatically generates and reads from an `Input` directory, and outputs to an `Output` directory. The user simply places a single Markdown file in the `Input` folder and hits Enter.

## [v1.8]

### Fixed

- **Filename Sanitization:** The app now aggressively strips leading and trailing markdown formatting characters (including asterisks `*`, underscores `_`, dashes `-`, tildes `~`, and backticks ```) from the extracted headers. This ensures that these symbols are completely removed from the generated filenames for both individual and A-Z exports.

## [v1.7]

### Fixed

- **A-Z Sorting with Markdown Syntax:** Fixed a bug in the A-Z export mode where headers starting with Markdown styling syntax (such as `Bold` or `_Italic_`) were being incorrectly sorted into the `Misc.md` file. The app now intelligently searches for the first alphanumeric character to determine grouping.

## [v1.6]

### Added

- **Header Level Conversion:** Added an optional prompt to convert the targeted split headers to a different level upon export (e.g., converting an H3 split to an H1 in the newly created file).
- Added a console warning clarifying that header conversion only affects the specific headers where the split occurs, leaving all nested sub-headers completely intact.

## [v1.5]

### Changed

- **Filename Formatting:** The app now automatically replaces any spaces with underscores (`_`) in the generated output filenames (applies to both prefixes and header names).

## [v1.4]

### Changed

- **Refined A-Z Export:** The script now strictly limits empty placeholder file generation to missing alphabetical letters (A-Z) only. It will no longer generate empty files for numbers (`0-9`) or the `Misc` category if no matching headers exist.

## [v1.3]

### Added

- **Visual Progress Reporting:** Added detailed console output during the export phase, displaying `-> Created: [filepath]`as each individual file is generated.
- Added a summary stat at the end of the process displaying the total number of sections processed.

## [v1.2]

### Fixed

- **Prompt Order Restoration:** Reverted the prompt sequence back to the original logical order (Filename -> Header Level -> Export Type -> Prefix) to prevent users from accidentally skipping the header selection and triggering unintended defaults.

### Changed (from unversioned hotfix)

- **Whitespace Management:** Implemented strict `.strip()` formatting on all extracted text chunks. This eliminates the massive trailing blank line gaps that were occurring between split sections, ensuring flush and clean Markdown exports.

## [v1.1]

### Added

- **A-Z Grouping Export Mode:** Introduced a secondary export type that alphabetically compiles all sections into grouped files (`A.md`, `B.md`, `Z.md`), numbers (`0.md` to `9.md`), and a `Misc.md` file. Missing alphabetical letters are automatically populated with placeholder text.
- **Custom Prefixes:** Added an optional prompt allowing users to prepend a custom string (e.g., `Magic Spells - `) to all exported filenames.
- **Continuous Workflow:** Encased the main script in a `while True` loop, prompting the user if they want to process another batch of files before quitting the app.

## [v1.0]

### Added

- Initial creation of `splitPhorge.py`.
- Core functionality to non-destructively parse and split Markdown documents based on specific heading levels (H1 through H6).
- Automatic generation of the destination directory.
- Exports individual Markdown files dynamically named using their corresponding header text.