import sys
import os
import yaml

class Plane:

    def __init__(self, filepath):
        self.config_file = './codes.yaml'
        self.filepath= filepath

    def get_yaml(self):
        with open(self.config_file) as file:
            full_codes = yaml.load(file)      # Get codes from config yaml file
            return full_codes
        return None

    def decode_this(self):
        res = os.system('python2 ./img_to_data/pdf417.py ' + self.filepath  + ' > key.txt')  # not secure but... who cares ? 
        fd = open('key.txt', 'r')
        text = fd.read()
        text = text.replace('\t', '')
        text = text.replace('\n', '')
        text = 'M' + text  # Sometimes the first M is not read so I add it manually
        table = text.split(' ')
        return table

    def get_company(self, code, full_codes):
        op = ''
        if len(code) == 8:
            op = code[6] + code[7]
        elif len(code) == 9:
            op = code[6] + code[7] + code[9]
        
        comp = full_codes.get(op)
        if comp is None:
            comp = full_codes.get('Default')
        
        print(comp)
        return comp


    def give_me_business_class(self, decoded_code_bar, full_codes):
        # Getting the right company to replace the with the good option
        company = self.get_company(decoded_code_bar[2], full_codes)  

        case = decoded_code_bar[4]
        julian_date = case[0] + case[1] + case[2]
        classe = case[3]     
        seat = case[4] + case[5] +case[6] + case[7]

        print('Actual Company  :' + company.get('name'))
        print('Business Class for this company : ' + company.get('business'))
        
        print('\nActual classe : ' + classe)
        print('Actual seat : ' + seat)
        
        classe = company.get('business')
        # Seat is currently 003B because business class is often within first numbers
        seat = '003B'

        print('\nNew classe : ' + classe)
        print('New seat : ' + seat)

        # Reformat to string
        seq = ''
        business = seq.join(decoded_code_bar)
        return business

    def create_codebar_from_data(self, business_code_bar):
        os.system('pdf417gen encode -o ' + os.path.splitext(self.filepath)[0] + '-modified.png ' + '"' + business_code_bar + '"')
        return

    def fly(self):
        full_codes = self.get_yaml()
        if full_codes is not None:
            decoded_code_bar = self.decode_this()
            business_code_bar = self.give_me_business_class(decoded_code_bar, full_codes)
            self.create_codebar_from_data(business_code_bar)