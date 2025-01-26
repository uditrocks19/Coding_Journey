# https://www.hackerrank.com/challenges/three-month-preparation-kit-two-characters/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-nine

un_set = set(s)
    mx = 0
    for ch1 in un_set:
        for ch2 in un_set:
            if ch1 != ch2:
                fil_string = [ch for ch in s if ch in(ch1, ch2)]
                is_valid = True
                for i in range(1, len(fil_string)):
                    if fil_string[i] == fil_string[i-1]:
                        is_valid = False
                        break
                if is_valid:
                    mx = max(mx, len(fil_string))

    return mx
