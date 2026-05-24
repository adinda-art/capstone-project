from src.preprocess import bersihkan_teks

def test_bersihkan_teks():
    # Menguji apakah fungsi mengubah teks menjadi huruf kecil semua
    assert bersihkan_teks("  DATA Capstone  ") == "data capstone"
