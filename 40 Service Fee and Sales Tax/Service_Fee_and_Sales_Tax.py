def servicesAndSalesTasks(n):
    totalServices = n + .10 * n
    totalSales = totalServices + .16 * totalServices

    return totalSales

print(servicesAndSalesTasks(100))