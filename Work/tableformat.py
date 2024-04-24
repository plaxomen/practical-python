# tableformat.py


class TableFormatter:
    def headings(self, headers):
        """Emit the table headings"""
        raise NotImplementedError()

    def row(self, rowdata):
        """Emit a single row of table data"""
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        """Emit the text table headings."""
        for h in headers:
            print(f"{h:>10s}", end=" ")
        print()
        print(("-" * 10 + " ") * len(headers))

    def row(self, rowdata):
        """Emit the row of text."""
        for cell in rowdata:
            print(f"{cell:>10s}", end=" ")
        print()


class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        """Emit the CSV formatted headings."""
        print(",".join(headers))

    def row(self, rowdata):
        """Emit the CSV formatted row of data."""
        print(",".join(rowdata))


class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        """Emit an HTML formatted header of table data."""
        # Creating table head and row opening tags.
        thead = "<thead><tr>"
        for h in headers:
            thead += f"<th>{h}</th>"

        # Close table head and row tags.
        thead += "</tr></thead>"
        print(thead)

    def row(self, rowdata):
        """Emit an HTML formatted row of table data."""
        tr = "<tr>"
        for td in rowdata:
            tr += f"<td>{td}</td>"
        tr += "</tr>"
        print(tr)
