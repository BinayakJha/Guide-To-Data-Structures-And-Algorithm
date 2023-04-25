# @param {number} total_versions
# @return {number}
def first_bad_bersion(total_versions):
    start = 1
    end = total_versions
    while start < end:
        midpoint = start + int((end - start) / 2)
        print(midpoint)
        if is_bad_version(midpoint): # if midpoint is bad, then the first bad version is before midpoint
            end = midpoint
        else:
            start = midpoint + 1
    return start
def is_bad_version(version):
    if version >= 6:
        return True
    else:
        return False

total_versions = 10
print(first_bad_bersion(total_versions))