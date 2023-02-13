import os
import json
import string



class Scanner(object):
    
    
    def __init__(self):
        
        super(Scanner, self).__init__()
        
        self.available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
    
    def init(self):
        
        cursor = {
            'object' : {
                'found' : {
                    'drive' : None,
                    'root'  : [],
                    'dirs'  : [],
                    'files' : []
                }
            }
        }
        
        data = []
        
        for drive in self.available_drives:
            
            drive = os.path.normpath(drive)
            
            cursor['object']['found']['drive'] = drive
            
            for root, dirs, files in os.walk(drive):
                
                root = os.path.normpath(root)
                
                cursor['object']['found']['root'], cursor['object']['found']['dirs'], cursor['object']['found']['files'] = root, dirs, files
                
                data.append(json.dumps(cursor, indent = 4, sort_keys = True))
        
        
        with open('data.json', 'w') as data_file:
            data_file.write('{\n')
            
            for line in data:
                
                line = str(line + ',\n')
                
                data_file.write(line)
                
            data_file.write('\n}')
                
        data_file.close()
        
            


if __name__ == '__main__':
    Scanner().init()