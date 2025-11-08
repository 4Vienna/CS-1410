class YouTubeChannel:
    name: str
    video_count: int
    def __init__(self, name="", video_count=0):
        '''
        name: the channel title  
        video_count: number of videos uploaded to this channel  
        '''
        self._name = name
        self.__video_count = video_count

    def get_name(self) -> str:
        """Return the channel name."""
        return self._name
    
    def set_name(self, name: str) -> None:
        """Set the channel name."""
        self._name = name

    def get_video_count(self) -> int:
        """Return the number of videos."""
        return self.__video_count
    
    def set_video_count(self, count: int) -> None:
        """Set the number of videos."""
        if count >= 0:
            self.__video_count = count
        else:
            raise ValueError("Video count cannot be negative.")

    def __str__(self) -> str:
        return f"Channel: {self._name}, Videos: {self.__video_count}"
    

def main():
    channel = YouTubeChannel("UVUCS1410", 150)
    print(channel)

    print(f"Channel Name: {channel.get_name()}")
    print(f"Number of Videos: {channel.get_video_count()}")

    channel.set_name("Changed Name")
    channel.set_video_count(20)

    print(f"Channel Name: {channel.get_name()}")
    print(f"Number of Videos: {channel.get_video_count()}")

    # Reflection Question 1 Proof
    print(f"Direct Access Name: {channel._name}")
    channel._name = "Directly Changed Name"
    print(channel)

    # Reflection Question 2 Proof
    #print(f"Direct Access Video Count: {channel.__video_count}")
    # This raises an AttributeError because __video_count is name-mangled
    print(f"Accessing Video Count via Name Mangling: {channel._YouTubeChannel__video_count}")
    channel._YouTubeChannel__video_count = 1 
    print(channel)

if __name__ == "__main__":
    main()