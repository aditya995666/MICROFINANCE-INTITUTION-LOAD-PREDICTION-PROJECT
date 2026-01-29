import tabula as tb
import pandas as pd
import tempfile

def read_pdf(uploaded_file):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.read())
            temp_path = tmp.name

        dfs = tb.read_pdf(
            temp_path,
            pages="all",
            multiple_tables=True
        )

        if dfs:
            return pd.concat(dfs, ignore_index=True)
        return None

    except Exception as e:
        print("PDF Read Error:", e)
        return None
