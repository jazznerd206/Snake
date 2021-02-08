# BYTE_SYZE
# You must build a input field which accepts
# values up to size 160
# TWIST
# size doesn't refer to length, but 
# byte syze instead

# snake_bytes(stryng)

def can_post_to_feed(string):
    def snake_bytes(string):
        return(len(string.encode('utf-8')))
    if (snake_bytes(string) < 40):
        print('true')
        return True
    print('false')
    return False


can_post_to_feed('😀')
can_post_to_feed('😀')
can_post_to_feed('😀😀')
can_post_to_feed('😀😀😀')
can_post_to_feed('😀😀😀😀😀😀😀')
can_post_to_feed('😀😀😀😀😀😀😀😀😀😀😀😀') # returns false, emoji is worth 4 UTF8 characters
can_post_to_feed('1,2,3,4,5,6,7,8,9,10,11')