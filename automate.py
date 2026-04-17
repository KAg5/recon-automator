import subprocess
import sys

cmd =  "/home/kali/go/bin/./httpx -fr -rlm 5 -sc -td -title -server -ip -cdn -random-agent -l sub1.txt -o sub-info.txt"
cmd1 = 'cat sub1.txt | httpx-toolkit -o alivesub.txt'
cmd2 = "cat alivesub.txt | waybackurls | tee urls.txt"
cmd3 = 'cat urls.txt | grep -iE ".js" | grep -ivE ".json" | sort -u | tee js.txt'
cmd4 = 'cat urls.txt | grep "=" | tee param.txt'


print("type full url with domain name:")
target = input()


subprocess.run(['bash', '/home/kali/tools/SubEnum/./subenum.sh', '-d', target ,'-e', 'Amass', '-o','sub1.txt'], capture_output=False, text=True)

print("\nproceeding with subdomain information checking")

try:
    subprocess.run([cmd], capture_output=False, text=True,shell=True )
except KeyboardInterrupt:
    print("\nInterrupt received! Stopping...")
except Exception as e:
    print("\nerror while subdomain info checking:", e)


subprocess.run([cmd1], capture_output=False, text=True,shell=True )

print("do you want to proceed with waybackurls: type y or n")
choice = input()

if choice == 'y':
    try:

        subprocess.run([cmd2], capture_output=False, text=True, shell=True)
    except KeyboardInterrupt:
        print("\nInterrupt received! Stopping...")
    except Exception as e:
        print("\nerror while url surfing:", e)

else:
    sys.exit(0)


print("\nSorting js files in one file....\n")
subprocess.run([cmd3], capture_output=False, text=True,shell=True )

print("\nsorting urls with param in them...")
subprocess.run([cmd4], capture_output=False, text=True,shell=True )