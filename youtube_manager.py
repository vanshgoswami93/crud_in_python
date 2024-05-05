import json

filename = 'youtube.txt'

def load_data():
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open(filename, 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("*" * 80)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']} - {video['time']}")
    print("\n")
    print("*" * 80)

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")

    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos()
    index = int(input("Enter the video number you want to update"))
    if 1 <= index <= len(videos):
        name = input("Enter new video name")
        time = input("Enter the new video time")
        videos[index - 1] = {'name': name, 'time': time}
        save_data_helper(videos)
    else:
        print("Invalid index selected")

def delete_video(videos):
    list_all_videos()
    index = int(input("Enter the video number you want to delete"))

    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data_helper(videos)
    else:
        print("Invalid index selected")


def main():

    videos = load_data()
    while True:

        print("\n ********YOUTUBE MANAGE********  \n Please select from below options")
        print("1. List all favourite videos")
        print("2. Add to the favourite videos")
        print("3. Edit a favourite video")
        print("4. Delete or Romove from favourite videos")
        print("5. Exit the app")

        choice = input("Enter your choice here: ")


        if choice == '1':
            list_all_videos(videos)
        elif choice == '2':
            add_video(videos)
        elif choice == '3':
            update_video(videos)
        elif choice == '4':
            delete_video(videos)
        elif choice == '5':
            print("Exiting the app. Goodbye!")
            break
        else:
            print('Invalid Choice')


if __name__ == "__main__":
    main()
