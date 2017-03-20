import os, shutil, time

class TextbookHandler:
    '''
    Handles loading of textbooks onto flash drive.
    '''

    def __init__(self, path_to_drives='/Volumes/', path_to_textbooks='/Users/joshuachen/Google Drive/Textbooks'):
        print 'Initializing handler...'
        self.start_drives = os.listdir(path_to_drives)
        self.curr_drives = os.listdir(path_to_drives)
        self.new_drives = []
        self.removed_drives = []
        self.path_to_textbooks = path_to_textbooks
        print 'Finished initialization of handler.'

    def get_curr_drives(self):
        return os.listdir('/Volumes/')

    def update_new_drives(self):
        self.curr_drives = self.get_curr_drives()

        for drive in self.curr_drives:
            if drive not in self.start_drives:
                self.new_drives.append(drive)

    def update_removed_drives(self):
        self.curr_drives = self.get_curr_drives()

        for drive in self.start_drives:
            if drive not in self.curr_drives:
                self.removed_drives.append(drive)

    def handle_new_drives(self, status=False):
        for drive in self.new_drives:
            print 'New drive: ', drive

            print 'Waiting for drive verification...'
            print 'In',
            for i in range(3, 0, -1):
                if (i != 3):
                    print '  ',
                print i, '...'
                time.sleep(1)

            print 'Please do not remove your drive...'
            try:
                self.load_new_drive(drive, status)
            except OSError:
                pass

    def load_new_drive(self, drive, status=False):
        contents = os.listdir('/Volumes/' + drive)
        path_to_textbooks = '/Volumes/' + drive + '/Textbooks/'

        print 'Checking if directory "Textbooks" exists...'
        if 'Textbooks' not in contents:
            print 'Creating new directory "Textbooks"...'
            os.makedirs(path_to_textbooks)
            print 'Adding files to directory "Textbooks"...'
        else:
            print 'Updating directory "Textbooks"...'

        # Filter out files with ".pdf" extension
        textbooks = [tb for tb in os.listdir(self.path_to_textbooks) if len(tb) >= 4 and tb[-4:] == '.pdf']
        
        for tb in textbooks:
            # Check if in contents
            if tb not in contents:
                # Print out status message
                if status:
                    print '\tCopying "' + tb + '"... \t (%d / %d) [%.2f%%]' % (len(os.listdir(path_to))+1, len(os.listdir(path_to_textbooks)), 100*(float(len(os.listdir(path_to))+1)) / len(textbooks))
                # Copy textbook
                shutil.copy2(self.path_to_textbooks + tb, path_to_textbooks)
                # Update contents
                contents = os.listdir('/Volumes/' + drive)

        print 'Checking that all files were updated successfully...'
        if self.check_new_drive(path_to_textbooks, self.path_to_textbooks):
            print 'Success!'
        else:
            print 'Failure.'

    def check_new_drive(self, path1, path2):
        contents1, contents2 = os.listdir(path1), os.listdir(path2)

        return set(contents1) == set(contents2)

    def handle_removed_drives(self):
        for drive in self.removed_drives:
            print 'Removed drive:', drive

    def update_start_drives(self):
        if self.start_drives != self.curr_drives:
            self.start_drives = self.curr_drives

    def run(self):
        while 1:
            self.update_new_drives()
            self.update_removed_drives()
            self.handle_new_drives(True)
            self.handle_removed_drives()
            self.update_start_drives()


if __name__ == '__main__':
    # print 'Running...'
    # start_drives = os.listdir('/Volumes/')

    # while 1:
    #     curr_drives = os.listdir('/Volumes/')
    #     # Keep track of new and removed drives
    #     new_drives, removed_drives = [], []

    #     for drive in curr_drives:
    #         if drive not in start_drives:
    #             new_drives.append(drive)

    #     for drive in start_drives:
    #         if drive not in curr_drives:
    #             removed_drives.append(drive)

    #     for drive in new_drives:
    #         print 'New drive: ', drive

    #         print 'Waiting for drive verification...'
    #         print 'In',
    #         for i in range(3, 0, -1):
    #             if (i != 3):
    #                 print '  ',
    #             print i, '...'
    #             time.sleep(1)

    #         try:
    #             files = os.listdir('/Volumes/' + drive)
    #             print 'Checking if directory "Textbooks" exists...'
    #             if 'Textbooks' not in files:
    #                 print 'Creating new directory "Textbooks"...'
    #                 os.makedirs('/Volumes/' + drive + '/Textbooks')
    #                 print 'Adding files to directory "Textbooks"...'
    #             else:
    #                 print 'Updating directory "Textbooks"...'

    #             path_to = '/Volumes/' + drive + '/Textbooks'
    #             path_to_textbooks = '/Users/joshuachen/Google Drive/Textbooks/'
    #             textbooks = os.listdir('/Users/joshuachen/Google Drive/Textbooks/')
    #             textbooks = [tb for tb in textbooks if len(tb) >= 4 and tb[-4:] == '.pdf']
    #             for tb in textbooks:
    #                 if tb not in os.listdir(path_to):
    #                     print '\tAdding "' + tb + '"... \t (%d / %d) [%.2f%%]' % (len(os.listdir(path_to))+1, len(os.listdir(path_to_textbooks)), 100*(float(len(os.listdir(path_to))+1)) / len(textbooks))
    #                     shutil.copy2(path_to_textbooks + tb, path_to)

    #             print 'Checking that all files were updated successfully...'
    #             if set(os.listdir(path_to)) == set(textbooks):
    #                 print 'Good!'
    #             else:
    #                 print 'Bad!'
    #         except OSError:
    #             pass

    #     for drive in removed_drives:
    #         print 'Removed drive: ', drive

    #     if (start_drives != curr_drives):
    #         start_drives = curr_drives
    tbh = TextbookHandler()
    tbh.run()
