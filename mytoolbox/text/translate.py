import subprocess

def translate(x,src="fr",dest="en",engine ="bing"):
    try:
        return subprocess.check_output(["trans","-b","-e",engine,"{0}:{1}".format(src,dest),"{0}".format(x)]).decode().strip().strip("\"")
    except:
        return x