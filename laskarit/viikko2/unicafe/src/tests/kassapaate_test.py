import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
        self.koyha_maksukortti = Maksukortti(100)

    def test_pohjakassa(self):
         self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_luotu_syödyt_edulliset(self):
         self.assertEqual(self.kassapaate.edulliset, 0)

    def test_luotu_syödyt_maukkaat(self):
         self.assertEqual(self.kassapaate.maukkaat, 0)
     
    def test_onko_vaihtoraha_oikein_maukas(self):
         self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(1000), 600)

    def test_onko_vaihtoraha_oikein_edullinen(self):
         self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(1000), 760)

    def test_onko_kassa_oikein_maukas(self):
         self.kassapaate.syo_maukkaasti_kateisella(1000)
         
         self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_onko_kassa_oikein_edullinen(self):
         self.kassapaate.syo_edullisesti_kateisella(1000)
         
         self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
    
    def test_onko_maara_oikein_maukas(self):
         self.kassapaate.syo_maukkaasti_kateisella(1000)
         
         self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_onko_maara_oikein_edullinen(self):
         self.kassapaate.syo_edullisesti_kateisella(1000)
         
         self.assertEqual(self.kassapaate.edulliset, 1)

    #--- case liian vähän rahaa
         
    def test_onko_vaihtoraha_oikein_maukas_liian_vahan_rahaa(self):
         self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(100), 100)

    def test_onko_vaihtoraha_oikein_edullinen_liian_vahan_rahaa(self):
         self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100), 100)

    def test_onko_kassa_oikein_maukas_liian_vahan_rahaa(self):
         self.kassapaate.syo_maukkaasti_kateisella(100)
         
         self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_onko_kassa_oikein_edullinen_liian_vahan_rahaa(self):
         self.kassapaate.syo_edullisesti_kateisella(100)
         
         self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_onko_maara_oikein_maukas_liian_vahan_rahaa(self):
         self.kassapaate.syo_maukkaasti_kateisella(100)
         
         self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_onko_maara_oikein_edullinen_liian_vahan_rahaa(self):
         self.kassapaate.syo_edullisesti_kateisella(100)
         
         self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaiden_osto_kortilla_rahaa(self):
         self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
         
    def test_edullisten_osto_kortilla_rahaa(self):
         self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)

    def test_maukkaiden_osto_kortilla_rahaa_myytyjen_maara_kasvaa(self):
         self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

         self.assertEqual(self.kassapaate.maukkaat, 1)
         
    def test_edullisten_osto_kortilla_rahaa_myytyjen_maara_kasvaa(self):
         self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

         self.assertEqual(self.kassapaate.edulliset, 1)
     

    def test_maukkaiden_osto_kortilla_ei_rahaa(self):
         self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.koyha_maksukortti), False)
         
    def test_edullisten_osto_kortilla_rahaa(self):
         self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.koyha_maksukortti), False)

    def test_maukkaiden_osto_kortilla_rahaa_myytyjen_maara_ei_kasva(self):
         self.kassapaate.syo_maukkaasti_kortilla(self.koyha_maksukortti)

         self.assertEqual(self.kassapaate.maukkaat, 0)
         
    def test_edullisten_osto_kortilla_rahaa_myytyjen_maara_ei_kasva(self):
         self.kassapaate.syo_edullisesti_kortilla(self.koyha_maksukortti)

         self.assertEqual(self.kassapaate.edulliset, 0)
     
    def test_maukkaiden_osto_kortilla_kassa_ei_muutu(self):
         self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

         self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
         
    def test_edullisten_osto_kortilla_kassa_ei_muutu(self):
         self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

         self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_lataa_rahaa_kortille_kortin_saldo_muuttuu(self):
         self.kassapaate.lataa_rahaa_kortille(self.koyha_maksukortti,100)

         self.assertEqual(self.koyha_maksukortti.saldo_euroina(), 2.0)

    def test_lataa_rahaa_kortille_kassan_saldo_muuttuu(self):
         self.kassapaate.lataa_rahaa_kortille(self.koyha_maksukortti,100)

         self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1001.0)


    def test_lataa_rahaa_kortille_kortin_saldo_ei_muutu(self):
         self.kassapaate.lataa_rahaa_kortille(self.koyha_maksukortti,-100)

         self.assertEqual(self.koyha_maksukortti.saldo_euroina(), 1.0)

    def test_lataa_rahaa_kortille_kassan_saldo_ei_muutu(self):
         self.kassapaate.lataa_rahaa_kortille(self.koyha_maksukortti,-100)

         self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

