import flwr as fl

# Federated Averaging stratejisi ile sunucuyu başlat
def main():
    # FedAvg algoritmasını kullanacak şekilde bir strateji oluştur
    strategy = fl.server.strategy.FedAvg(
        fraction_fit=1.0,  # Her turda tüm uygun istemcileri eğitim için kullan
        fraction_evaluate=1.0,  # Her turda tüm uygun istemcileri değerlendirme için kullan
        min_fit_clients=2,  # Eğitim için minimum istemci sayısı
        min_evaluate_clients=2,  # Değerlendirme için minimum istemci sayısı
        min_available_clients=2,  # Bağlantı için beklenen minimum istemci sayısı
    )

    # Sunucuyu başlat
    fl.server.start_server(
        server_address="0.0.0.0:8080",
        config={"num_rounds": 5},  # Eğitim turu sayısı
        strategy=strategy,
    )

if __name__ == "__main__":
    main()
