for ($i = 1; $i -le 25; $i++) {
    # Create a folder for each day
    New-Item -ItemType Directory -Path "./day_$i" -Force

    # Create two empty python files in each of the directories
    New-Item -ItemType File -Path "./day_$i/part_1.py"
    New-Item -ItemType File -Path "./day_$i/part_2.py"
}