import os

def get_enemynames(folderpath, output_file="EnemyNames.txt"): #Used to Create a List of names to write all 
    try:
        items = os.listdir(folderpath)

        for item in items:
            print(item)

        with open(output_file,"w") as output:
            for item in items:
                output.write(item + "\n")

    except Exception as e:
        print(e)

if __name__ == "__main__":
    folderpath = "D:\Coding\HolocureAutoFarmBot\images\in_game\Enemies"
    get_enemynames(folderpath)