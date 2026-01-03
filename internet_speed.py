import speedtest

def test_internet_speed():
    print("📡 Testing internet speed...\n")

    st = speedtest.Speedtest()
    st.get_best_server()

    ping = st.results.ping
    download = st.download() / 1_000_000  # Mbps
    upload = st.upload() / 1_000_000      # Mbps

    print(f"🏓 Ping     : {ping:.2f} ms")
    print(f"⬇️ Download : {download:.2f} Mbps")
    print(f"⬆️ Upload   : {upload:.2f} Mbps")

if __name__ == "__main__":
    test_internet_speed()
