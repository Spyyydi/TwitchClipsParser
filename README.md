# Instructions for Parsing Clips

Follow these steps to extract and analyze clips data from the Creator Dashboard:

## Steps to Export Clips Data

1. **Navigate to Clips Section**:
   - Go to `Creator Dashboard` -> `Clips` -> `Clips I've created`.

2. **Collapse Any Expanded Clips**:
   - Ensure that any expanded clips are collapsed to avoid extracting unnecessary data.

3. **Scroll to the First Created Clip**:
   - Scroll down to the first clip you’ve created. You can use the middle mouse button to auto-scroll for convenience.

4. **Inspect and Copy HTML Element**:
   - Right-click on the page and select `Inspect` to open the browser’s Developer Tools.
   - In the `Elements` tab, right-click on the topmost HTML element and select `Copy` -> `Copy element` to copy the HTML.

5. **Save HTML to File**:
   - Paste the copied HTML element into a file named `clips.txt`.

6. **Run the Script**:
   - Ensure that both `clipsParser.py` and `clips.txt` are in the same directory.
   - Run the script to parse the data.


## Output File Structure

```
Total channels: {number}
Total clips: {number}
-------------------------
Channel name: {clips number}
-------------------------
Clip #{Clip number}
Clip name: {Clip Name}
Channel name: {Channel name}
Category name: {Category name}
-------------------------
```
