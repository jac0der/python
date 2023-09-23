"""
    Watch Over Me Song Details.
    Script outlining the details of one of my favourite
    songs using Python variables.
"""

# variable declarations

Title = "Watch Over Me"         # official name of the song
Artist = "Jermaine Edwards"     # name of singer who sang the song
Author = "Jermaine Edwards"     # the song writer
Genre = "Reggae Gospel"         # category the style of music the song falls under
Riddim = "watch"                # beat used to record song
Producer = "Romeich Entertainment & Island worship Productions" # Groups which sponsor the song
VideoProduction = "Iceyjace Films"  # Procucer/Director of the song's associated music video
Album = "Watch Over Me"         # Album/Disk song was released on
ReleaseYear = 2020              # Year song was released to the general public
Duration = 151                  # lenght of play of song in seconds
BeatMode = "Fast"               # pace of the song's beat
Cost = 2550.55                  # Price for one recording of the song
SaleCost = 1550.50              # Price of song whenever it is place on sale
Currency = "JMD"                # monetary unit for the cost of the song
Codec = "MPEG-1 Layer 3 (MP3)"  # encryption mode of song
Channel = 'Stereo'              # song audio playback format
SampleRate = 48000              # number of sample beats in song in Hz
PlayCount = 2346                # Total amount of time I have played song this week
FeaturesCount = 0               # number of additional artists on song
Features = "none"               # names of additional artists on song
CountryOfOrigin = "Jamaica"     # country which song is native of
StarRatings = 4.5               # public rating of song from a total of five stars

CopiesSold = 1254153            # total amount of copies of the song sold at regular cost,
                                            # NOT ON SALE
Revenue    = Cost * CopiesSold  # total monies gain from regular sales of the song

SaleCopiesSold = 2457861        # total amount of copies of the song sold on sale

SaleRevenue = SaleCost * SaleCopiesSold # total monies gain from SALE sales of the song

TotalRevenue = Revenue + SaleRevenue    # total earnings of song as at current date

firsNameInitial = 'J'
lastNameInitial = 'E'



"""
    variable print outs - labels are attached to the actual variable
    values for ease of read once printed out.
"""
print('Title: ', Title)
print('Artist: ', Artist)
print('Author: ', Author)
print('Genre: ', Genre)
print('Riddim: ', Riddim)
print('Producer: ', Producer)
print('Video Production: ', VideoProduction)
print('Album: ', Album)
print('Release Year: ', ReleaseYear)
print('Duration (secs): ', Duration)
print('Beat Mode: ', BeatMode)
print('Cost: ', Cost)
print('SaleCost: ', SaleCost)
print('Currency: ', Currency)
print('Codec: ', Codec)
print('Channel: ', Channel)
print('Sample Rate (Hz): ', SampleRate)
print('play Count: ', PlayCount)
print('Feature Count: ', FeaturesCount)
print('Features: ', Features)
print('Country of Origin: ', CountryOfOrigin)
print('Star Ratings: ', StarRatings)

print('Copies Sold: ', CopiesSold)
print('Revenue: ', Currency + f"{Revenue: ,}")      # formatting number to String for better display
                                                                # of figure, thus able to concatenate Currency value
                                                                # which is a String type as well.

print('Sale Copies Sold: ', SaleCopiesSold)
print('Sale Revenue: ', Currency + f"{SaleRevenue: ,}")    # formatting number for better display


print('Total Revenue: ', Currency + f"{TotalRevenue: ,}")  # formatting number for better display

print('Artist Initial: ', firsNameInitial + lastNameInitial)










