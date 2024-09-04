import getStatistics from "@/services/getStatistics"
import { useEffect, useState } from "react"
import { useQuery } from "@tanstack/react-query"

export default function useStatistics() {
  const [isEnabled, setIsEnabled] = useState(false)
  const [statisticsQuery, setStatisticsQuery] = useState<StatisticsQuery>({
    start_date: new Date(),
    end_date: new Date(),
    profit: true,
    annualized_return: false,
    percent_return: false
  })
  const [statisticsResult, setStatisticsResult] = useState<StatisticsResult | null>(null)

  const { error, data, isFetching } = useQuery({
    queryKey: ["statistics", statisticsQuery],
    queryFn: () => getStatistics(statisticsQuery.start_date, statisticsQuery.end_date, statisticsQuery.profit, statisticsQuery.annualized_return, statisticsQuery.percent_return),
    enabled: isEnabled
  })

  useEffect(() => {
    if (data) {
      setStatisticsResult(data)
    }
  }, [data])

  function handleSubmit(statistics: StatisticsQuery) {
    setStatisticsQuery(statistics)
    setIsEnabled(true)
  }

  return { statisticsResult, handleSubmit, isFetching, error }
}

export type StatisticsQuery = {
  start_date: Date
  end_date: Date
  profit: boolean
  annualized_return: boolean
  percent_return: boolean
}

export type StatisticsResult = {
  profit?: number
  annualized_return?: number
  percent_return?: number
}
