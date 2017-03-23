def textgrid_to_yaml(input_file, output_file):
    # Textgrid should be in chronological format
    with open(input_file) as f:
        data = f.read()
    data = data.split("\n")
    # Get the necessary info
    info = []
    for i in range(len(data)-2):
        if len(data[i]) > 0:
            if data[i][0] == "!" and len(data[i + 2]) != 2:
                timing = data[i + 1].split()
                start = float(timing[1])
                end = float(timing[2])
                title = data[i + 2].split()[-1]
                title = title.replace('"', '')
                title = title.replace('(', '')
                title = title.replace(')', '')
                info.append((title, start, end))
    # Format it nicely
    output = []
    for entry in info:
        line = "{}:\n sta: {}\n end: {}".format(entry[0], entry[1], entry[2])
        output.append(line)
    output = "\n".join(output)
    with open(output_file, "w") as f:
        f.write(output)
    print("Saved as", output_file)

input_file = "complete_annotated.TextGrid"
output_file = "complete_annotated.yaml"
textgrid_to_yaml(input_file, output_file)
