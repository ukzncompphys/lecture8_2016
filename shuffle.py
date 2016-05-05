import sounddevice as sd
import time,glob,numpy,random,subprocess

def get_key(mystr,key):  #routine to find a key in a long strong and return that line
    i1=mystr.find(key)
    i2=mystr.find('\n',i1+2)  #start from just past initial position, look for the next newline
    return mystr[i1+len(key):i2].strip()

def play_song(fname):
    faad='faad'
    to_exec=faad + ' -i '+ fname  #first, read header so we can report song info
    aa=subprocess.check_output(to_exec,stderr=subprocess.STDOUT,shell=True)
    nn=get_key(aa,'\ntitle:')  #we'll get name of song
    writer=get_key(aa,'\nwriter:')  #and composer

    myinfo=get_key(aa,'LC AAC') #we'll get some info about the file
    tags=myinfo.split()  #this splits strings into their pieces
    rate=tags[-2]
    nchan=tags[-4]
    length=tags[0]
    print 'playing ' + nn + ' by ' + writer + ' for ' + length + ' ' + tags[1]
    
    to_exec=faad+ ' -f2 -w -b4 ' + fname  #this magic command will have faad read data into float arrays
    ff=open('/dev/null','w')
    dd=subprocess.check_output(to_exec,stderr=ff,shell=True) #this calls faad to do the heavy lifting 
    ff.close()

    dat=numpy.fromstring(dd,dtype='float32') #convert string output from faad into numpy array
    nchan=numpy.int(nchan)
    dat=numpy.reshape(dat,[len(dat)/nchan,nchan])
    fs=numpy.int(rate) #get the sample rate the speakers are expecting
    sd.play(dat,fs,blocking=False) #play through speakers using sounddevice
    return numpy.float(length) #return length of song.  

if __name__=='__main__':
    dr='/Users/sievers/Music/ipod_touch/'
    fnames=glob.glob(dr + '/*/*.m4a') #get filenames from a directory
    random.shuffle(fnames) #randomly reorder the file names
    for fname in fnames: #loop over filenames in music library
        try:
            mylen=play_song(fname)  #play the song, and learn how long it is
            time.sleep(mylen)       #wait until the song should have finished
        except:  #when we get a ctrl-c, we'll jump here.  this just
            pass    #goes to next loop iteration, which overwrites current song

