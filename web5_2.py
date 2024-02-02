import sys

from Samples.geocoder import get_ll_span, get_coordinates
from Samples.mapapi_PG import show_map


def main():
    toponym = " ".join(sys.argv[1:])

    if toponym:
        l1, l2 = get_coordinates(toponym)
        request = f'll={l1},{l2}&spn=0.005,0.005'
        show_map(request, 'sat')

        ll, spn = get_ll_span(toponym)
        request = f'll={ll}&spn={spn}'
        show_map(request)

        show_map(request, 'map', add_params=f'pt={ll},comma')


if __name__ == '__main__':
    main()
