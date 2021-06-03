import logging

logging.basicConfig(level=logging.INFO, filename="app.log")


def main():
    sites = \
        {
            "za-gp-ran-": 4,
            "za-gp-pkl-": 6,
            "za-gp-bry-": 5,
            "za-wc-cpt-": 8,
            "za-wc-tgw-": 6,
            "za-gp-tis-": 6,
            "za-kzn-umh-": 8,
            "za-kzn-trv-": 6,

        }

    forbidden = \
        [
            "za-gp-ran-asw-3 Te0/0/0/0",
            "za-gp-pkl-asw-5 Te0/0/0/0",
            "za-gp-pkl-asw-5 Te0/0/0/14",
            "za-gp-pkl-asw-5 Te0/0/0/15",
            "za-gp-pkl-asw-5 Te0/0/0/16",
            "za-gp-pkl-asw-5 Te0/0/0/17",
            "za-gp-pkl-asw-5 Te0/0/0/18",
            "za-gp-pkl-asw-5 Te0/0/0/34",
            "za-gp-pkl-asw-6 Te0/0/0/24",
            "za-gp-pkl-asw-6 Te0/0/0/25",
            "za-gp-pkl-asw-6 Te0/0/0/26",
            "za-gp-pkl-asw-6 Te0/0/0/27",
            "za-gp-pkl-asw-6 Te0/0/0/28",
            "za-gp-bry-asw-5 Te0/0/0/33",
            "za-gp-tis-asw-5 Te0/0/0/14",
            "za-gp-tis-asw-5 Te0/0/0/47",
            "za-gp-tis-asw-6 Te0/0/0/24",
            "za-wc-cpt-asw-7 Te0/0/0/16",
            "za-wc-cpt-asw-7 Te0/0/0/40",
            "za-wc-cpt-asw-7 Te0/0/0/41",
            "za-wc-cpt-asw-8 Te0/0/0/24",
            "za-wc-cpt-asw-8 Te0/0/0/25",
            "za-wc-tgw-asw-1 Te0/0/0/7",
            "za-wc-tgw-asw-3 Te0/0/0/2",
            "za-wc-tgw-asw-5 Te0/0/0/5",
            "za-wc-tgw-asw-5 Te0/0/0/6",
            "za-wc-tgw-asw-5 Te0/0/0/47",
            "za-wc-tgw-asw-6 Te0/0/0/5",
            "za-wc-tgw-asw-6 Te0/0/0/6",
            "za-kzn-umh-asw-5 Te0/0/0/23",
            "za-kzn-umh-asw-6 Te0/0/0/24",
            "za-kzn-umh-asw-7 Te0/0/0/16",
            "za-kzn-trv-asw-5 Te0/0/0/12",
            "za-kzn-trv-asw-5 Te0/0/0/47"
        ]

    template_start = "<config xmlns=\"http://tail-f.com/ns/config/1.0\">\n" \
                     "  <devices xmlns=\"http://tail-f.com/ns/ncs\">"

    template_end = "\n  </devices>\n</config>\n"


    with open('commit.xml', 'w') as xml_file:

        xml_file.write(template_start)
        for site in sites:
            for y in range(sites[site]):
                pw = 1000 * (y + 1)
                for x in range(48):
                    if f"{site}asw-{y + 1} Te0/0/0/{x}" in forbidden:
                        xml_file.write(
                            f"\n    <!-- SKIPPING: {site}asw-{y + 1} Te0/0/0/{x} -->")
                    else:
                        logging.debug(f"pe {(1000 * (y + 1)) + x} asw-{y+1} 0/0/0/{x}")
                        xml_file.write( \
                            f"\n    <device>\n" \
                            f"      <name>{site}asw-{y + 1}</name>\n" \
                            f"      <config>\n" \
                            f"        <interface xmlns=\"http://tail-f.com/ned/cisco-ios-xr\">\n" \
                            f"          <TenGigE>\n" \
                            f"            <id>0/0/0/{x}</id>\n" \
                            f"            <mtu>9130</mtu>\n" \
                            f"          </TenGigE>\n" \
                            f"        </interface>\n" \
                            f"      </config>\n" \
                            f"    </device>\n" \
                            f"    <device>\n" \
                            f"      <name>{site}pe-1</name>\n" \
                            f"      <config>\n" \
                            f"        <interface xmlns=\"http://tail-f.com/ned/cisco-ios-xr\">\n" \
                            f"          <PW-Ether>\n" \
                            f"            <id>{(1000 * (y + 1)) + x}</id>\n" \
                            f"            <mtu>9130</mtu>\n" \
                            f"          </PW-Ether>\n" \
                            f"        </interface>\n" \
                            f"      </config>\n" \
                            f"    </device>\n" \
                            f"    <device>\n" \
                            f"      <name>{site}pe-2</name>\n" \
                            f"      <config>\n" \
                            f"        <interface xmlns=\"http://tail-f.com/ned/cisco-ios-xr\">\n" \
                            f"          <PW-Ether>\n" \
                            f"            <id>{(1000 * (y + 1)) + x}</id>\n" \
                            f"            <mtu>9130</mtu>\n" \
                            f"          </PW-Ether>\n" \
                            f"        </interface>\n" \
                            f"      </config>\n" \
                            f"    </device>"
                        )
                    # f"               <!-- SKIPPING: {site}asw-{y + 1} Te0/0/0/{x} -->")
                    # print(f"devices device {site} config interface pw-ether {pw + x} mtu 9130")

        xml_file.write(template_end)

if __name__ == '__main__':
    main()

# logging.debug(stuff)
