# Simple Instructions to Use vCard to CSV Script

1. **Open Terminal**:
   - Click on the **Spotlight Search** (magnifying glass in the top-right corner) or press `Command (⌘) + Space`.
   - Type **Terminal** and press `Enter`.

2. **Navigate to the Script Location**:
   - In the Terminal window, type the following command and press `Enter`:
     ```bash
     cd /Users/curtispenn/Downloads/vcard2csv
     ```

3. **Run the Script**:
   - If your vCard files are in a specific folder, type the command below, replacing `foldername` with the name of the folder containing your `.vcf` files:
     ```bash
     python3 vcard2csv.py /path/to/foldername output.csv
     ```
   - For example, if the folder is also in Downloads, it would look like:
     ```bash
     python3 vcard2csv.py /Users/curtispenn/Downloads/vcard-folder output.csv
     ```

4. **Check the Output**:
   - After running the command, check the `/Users/curtispenn/Downloads/vcard2csv` folder. You should see a file named `output.csv`.

5. **Open the CSV File**:
   - You can open `output.csv` with Excel or any spreadsheet application to view your contacts.

## Summary
Just open Terminal, navigate to the script, run the command with the folder of vCards, and you’re done! Let me know if you need any more help!
