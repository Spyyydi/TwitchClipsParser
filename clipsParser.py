from bs4 import BeautifulSoup

# Read the contents of the file
with open('clips.txt', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Navigate through the nested structure to find the relevant rows
# Start from the <div class="Layout-sc-1xcs6mc-0 flREvo"></div> element
flrevo_div = soup.find('div', class_='Layout-sc-1xcs6mc-0 flREvo')

if flrevo_div:
    # Find all rows within this div
    rows = flrevo_div.find_all('div', class_='Layout-sc-1xcs6mc-0 eAnYGM clmgr-table__row')
else:
    rows = []

# Dictionary to keep track of clip counts per channel
channel_clip_counts = {}

# List to store extracted data
clip_data = []

# Extract the required information from each row
for row in rows:
    # Extract clip name
    clip_name_element = row.find('h5', class_='CoreText-sc-1txzju1-0')
    clip_name = clip_name_element['title'] if clip_name_element else None

    # Extract the channel name
    channel_name_element = row.find('a', class_='ScCoreLink-sc-16kq0mq-0 eFqEFL tw-link')
    channel_name = channel_name_element['title'] if channel_name_element else None

    # Extract the category name
    category_name_element = row.find('a', class_='ScCoreLink-sc-16kq0mq-0 eFqEFL InjectLayout-sc-1i43xsx-0 fmrktE tw-link')
    category_name = category_name_element['title'] if category_name_element else None

    # Add clip data to list
    clip_data.append((clip_name, channel_name, category_name))

    # Update the clip count for the channel
    if channel_name in channel_clip_counts:
        channel_clip_counts[channel_name] += 1
    else:
        channel_clip_counts[channel_name] = 1

# Calculate the total number of channels
total_channels = len(channel_clip_counts)

# Calculate the total number of clips
total_clips = len(clip_data)

# Sort the channel names by clip counts in descending order, then alphabetically
sorted_channel_counts = sorted(channel_clip_counts.items(), key=lambda x: (-x[1], x[0]))

# Open the output file with UTF-8 encoding
with open('output.txt', 'w', encoding='utf-8') as output_file:
    # Write the total number of channels and clips
    output_file.write(f"Total channels: {total_channels}\n")
    output_file.write(f"Total clips: {total_clips}\n")
    output_file.write("-------------------------\n")

    # Write the sorted channel names and clip counts
    for channel_name, clip_count in sorted_channel_counts:
        output_file.write(f"{channel_name}: {clip_count}\n")

    output_file.write("\n-------------------------\n")  # Add a newline to separate counts from clip details

    count = 0
    # Write the extracted clip information to the output file
    for clip_name, channel_name, category_name in clip_data:
        count += 1
        output_file.write(f"Clip #{count}\n")
        output_file.write(f"Clip name: {clip_name}\n")
        output_file.write(f"Channel name: {channel_name}\n")
        output_file.write(f"Category name: {category_name}\n")
        output_file.write("-------------------------\n")
