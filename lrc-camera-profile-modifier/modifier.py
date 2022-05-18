import os, re

for dname, dirs, files in os.walk("./"):
    for fname in files:
        if fname.endswith(".xmp"):
            fpath = os.path.join(dname, fname)

            words = fname[:-4].split(" ")

            cname = ""
            pname = ""

            index = words.index("Camera")
            cname = " ".join(words[:index])
            pname = " ".join(words[index+1:])

            with open(fpath) as f:
                s = f.read()

            s = re.sub(r"crs:CameraModelRestriction=\".*\"", "crs:CameraModelRestriction=\"\"", s)
            s = re.sub(r"crs:CameraProfile=\".*\"", "crs:CameraProfile=\"\"", s)

            s = s.replace("<rdf:li xml:lang=\"x-default\">Camera "+pname+"</rdf:li>", "<rdf:li xml:lang=\"x-default\">"+pname+"</rdf:li>")
            s = s.replace("<rdf:li xml:lang=\"x-default\">Profiles</rdf:li>", "<rdf:li xml:lang=\"x-default\">"+cname+"</rdf:li>")

            with open(fpath, "w") as f:
                f.write(s)