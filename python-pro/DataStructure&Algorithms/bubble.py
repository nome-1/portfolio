vox = [4,3,1,2]
print(vox)
runs=0
change=0
box=0
for a in range(len(vox)):
    for i,b in enumerate(vox):
        if i==len(vox)-1:
            if change>0:
                runs += 1
                box+=change
                change=0
                break
            break
        if vox[i+1]<vox[i]:
            vox[i+1],vox[i]=vox[i],vox[i+1]
            change+=1
print(f"Array is sorted in {box} swaps.")
print(f"First Element: {vox[0]}")
print(f"Last Element: {vox[-1]}")

