import { BACKEND_URL } from "@/lib/constants";
import { format } from "date-fns";

export default function getStatistics(start_date: Date, end_date: Date, profit: boolean, annualized_return: boolean, percent_return: boolean) {
  const url = new URL(`${BACKEND_URL}`)
  url.searchParams.append("start_date", format(start_date, "yyyy-MM-dd"))
  url.searchParams.append("end_date", format(end_date, "yyyy-MM-dd"))

  if (profit) {
    url.searchParams.append("includes", "profit")
  }

  if (annualized_return) {
    url.searchParams.append("includes", "annualized_return")
  }

  if (percent_return) {
    url.searchParams.append("includes", "percent_return")
  }

  return fetch(url.toString()).then((res) => res.json())
}
