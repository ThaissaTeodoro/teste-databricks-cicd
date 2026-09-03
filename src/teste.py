print("=" * 50)
print("ESTEIRA GITHUB -> DATABRICKS FUNCIONANDO!")
print("=" * 50)

spark.sql("""
    SELECT
        current_timestamp() AS data_execucao,
        'Deploy realizado pelo GitHub Actions' AS mensagem
""").show(truncate=False)
