import pandas as pd
import requests
import io


def download_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check HTTP status code
        return pd.read_csv(io.StringIO(response.content.decode('utf-8')))
    except requests.exceptions.RequestException as e:
        print(f"Download failed: {e}")
        return None
    except pd.errors.ParserError as e:
        print(f"CSV parsing error: {e}")
        return None


def filter_and_sort_data(df, product_keyword, sort_column='GA', ascending=False):
    try:
        # Filter and sort data
        filtered_df = df[df['IBM Product'].str.contains(product_keyword, case=False)]
        sorted_df = filtered_df.sort_values(by=sort_column, ascending=ascending)
        return sorted_df[['IBM Product', 'VRM', 'PID', 'MTM', 'GA', 'EOS']]
    except KeyError as e:
        print(f"Data column does not exist: {e}")
        return None


def write_to_excel(data_list, output_file, sheet_name="Product_Lifecycle"):
    writer = pd.ExcelWriter(output_file, engine='xlsxwriter')
    start_row = 0
    for product_keyword, data in data_list:
        if data is not None:
            data.to_excel(writer, sheet_name=sheet_name, startrow=start_row, index=False)
            start_row += len(data) + 2  # Add some spacing between sections
    # Save the Excel sheet after all data is written
    writer.close()


if __name__ == "__main__":
    url = "https://www.ibm.com/support/pages/sites/default/files/product-lifecycle/ibm_product_lifecycle_list.csv"
    output_file = "IBM_Product_Lifecycle_Groups.xlsx"
    product_keywords = ['IBM Power '], ['Key lifecycle'], ['IBM MQ'], ['Tape'], ['Storwize']

    data_list = []
    data = download_data(url)
    if data is not None:
        for keyword_group in product_keywords:
            group_data = []
            for keyword in keyword_group:
                filtered_data = filter_and_sort_data(data.copy(), keyword)
                group_data.append(filtered_data)
            data_list.append((", ".join(keyword_group), pd.concat(group_data, ignore_index=True)))
        write_to_excel(data_list, output_file)