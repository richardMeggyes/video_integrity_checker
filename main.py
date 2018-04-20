import os


def main():
    folder_path = 'e:/HandBreak_Videos/'
    error_path = folder_path + 'error/'
    error_file_name = 'error.log'
    error_file_path = folder_path + error_file_name
    files = os.listdir(folder_path)
    files_num = len(files)
    progress = 0
    error_counter = 0

    for video_file in files:
        if '.log' not in video_file and not os.path.isdir(folder_path + video_file):
            progress += 1
            video_file_path = folder_path + video_file
            os.system('ffmpeg -v error -i "{}" -f null - 2>"{}"'.format(video_file_path, error_file_path))
            error_file_size = os.path.getsize(error_file_path)
            if error_file_size:
                error_counter += 1
                if not os.path.exists(error_path):
                    os.makedirs(error_path)
                os.rename(video_file_path, error_path + video_file)
                new_error_file = error_path + video_file[:-4] + '.log'
                os.rename(folder_path + error_file_name, new_error_file)
                print('Error found in video file integrity! Moved to error folder.')

            print('Files: {}/{} Errors: {} Error file size: {:5} File: {}'.format(progress, files_num, error_counter,
                                                                                  error_file_size, video_file))

    os.remove(error_file_path)


if __name__ == '__main__':
    main()
