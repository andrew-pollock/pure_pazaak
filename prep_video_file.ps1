
## Use ffmeg to crop the video
## I only care about the area that shows Pazaak
ffmpeg -i clip/to_crop.mp4 -filter:v "crop=w=710:h=530:x=100:y=100" outputs/cropped_vid.mp4

## Drop the frame rate from 30 fps to 15 fps
ffmpeg -i outputs/cropped_vid.mp4 -filter:v fps=fps=15 outputs/low_fps_vid.mp4

# Delete cropped_vid since it's not needed anymore
Remove-Item 'outputs/cropped_vid.mp4'