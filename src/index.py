from varasto import Varasto

def tervehdi():
    print("Tehdään yli pitkä rivi, josta pitäisi tulla herja, toivottavasti, kohta nähdään toimiiko tämä.")
    print("Tervetuloa varastoon!\nLuonnin jälkeen:")

def alusta_varastot():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)
    return mehua, olutta

def tulosta_alkutilanteet(mehua, olutta):
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")

def tulosta_olut_getterit(olutta):
    print("\nOlut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")

def mehun_testit(mehua):
    print("\nMehu setterit:")
    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}")
    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")

def virhetilanteet():
    print("\nVirhetilanteita:")
    print("Varasto(-100.0):")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7):")
    huono = Varasto(100.0, -50.7)
    print(huono)

def paivita_olutta(olutta):
    print(f"\nOlutvarasto: {olutta}")
    print("olutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}")

def mehun_virheellinen_paivitys(mehua):
    print("\nMehuvarasto:")
    print("mehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}")

def oluen_virheellinen_nosto(olutta):
    print(f"\nOlutvarasto: {olutta}")
    print("olutta.ota_varastosta(1000.0)")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {olutta}")

def mehun_virheellinen_nosto(mehua):
    print(f"\nMehuvarasto: {mehua}")
    print("mehua.ota_varastosta(-32.9)")
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {mehua}")

def main():
    tervehdi()
    mehua, olutta = alusta_varastot()
    tulosta_alkutilanteet(mehua, olutta)
    tulosta_olut_getterit(olutta)
    mehun_testit(mehua)
    virhetilanteet()
    paivita_olutta(olutta)
    mehun_virheellinen_paivitys(mehua)
    oluen_virheellinen_nosto(olutta)
    mehun_virheellinen_nosto(mehua)

if __name__ == "__main__":
    main()
