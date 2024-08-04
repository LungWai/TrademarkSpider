import json

class JsonViser:
    def __init__(self, input_path, output_path, k=9):
        self.input_path = input_path
        self.output_path = output_path
        self.k = k  # Make k a class attribute

    def compare_json_strings(self, json_str1, json_str2):
        try:
            obj1 = json.loads(json_str1)
            obj2 = json.loads(json_str2)
            return obj1 == obj2
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return False

    def get_first_k_jsonlines(self, write_flag=False):
        jsonlines = []
        print("in get_first_k_jsonlines function")
        with open(self.input_path, 'r', encoding='utf-8') as file:
            print(f"self.input_path: {self.input_path}")
            first_line = file.readline()
            if not first_line:
                print("Input file is empty or unreadable.")
                return jsonlines  # Early return if file is empty
        # If the file is not empty, put the first line back and continue
            file.seek(0)
            if self.k == -1:  # If k is -1, read all lines
                jsonlines = [line.strip() for line in file]
            else:
                for i, line in enumerate(file):
                    print("in append function")
                    if i >= self.k:  # Adjusted to use >= to correctly limit to k lines
                        break
                    jsonlines.append(line.strip())
            if write_flag:
                # print(jsonlines)
                with open(self.output_path, 'w', encoding='utf-8') as file:
                    for line in jsonlines:
                        file.write(line + '\n')
        return jsonlines

    def execute_comparison(self):
        before = self.get_first_k_jsonlines(write_flag=False)  # Corrected to use write_flag parameter
        print("Before removing empty attributes:    {}".format(before[0] if before else "No data"))
        after = self.get_first_k_jsonlines(write_flag=False)  # Corrected to use write_flag parameter
        print("After removing empty attributes:    {}".format(after[0] if after else "No data"))
        if before and after:  # Check if both lists are not empty
            print(self.compare_json_strings(before[0], after[0]))
        else:
            print("One of the files is empty or does not contain enough lines.")

if __name__ == '__main__':
    extractor = JsonViser('trademark5\\trademark5.jsonlines', 'trademark5\\fewLine.jsonlines', 3)
    print(extractor.get_first_k_jsonlines(write_flag=True))

