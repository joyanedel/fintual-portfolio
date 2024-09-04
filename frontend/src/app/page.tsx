"use client"

import { useState } from "react"
import { sub, subDays } from "date-fns"
import { DateRange } from "react-day-picker"

import { Calendar } from "@/components/ui/calendar"
import { Label } from "@/components/ui/label"
import { Switch } from "@/components/ui/switch"


export default function Home() {
  const [date, setDate] = useState<DateRange | undefined>({
    from: subDays(new Date(), 30),
    to: new Date(),
  })

  return (
    <main className="flex-col w-full">
      <header className="pb-4">
        <h1 className="text-center text-3xl">Welcome to Fintual Portfolio Sandbox</h1>
        <h6 className="text-center">Here you will be able to calculate the profit within a time period, annualized return and percent return</h6>
      </header>

      <form className="flex justify-evenly items-start">
        <section aria-label="Date range picker">
          <Calendar
            mode="range"
            className="rounded-md"
            numberOfMonths={2}
            selected={date}
            onSelect={setDate}
            disabled={{after: new Date(), before: new Date(2021, 0, 1)}}
            fromDate={new Date(2021, 0, 1)}
            toDate={new Date()}
            defaultMonth={sub(new Date(), { months: 1 })}
          />
        </section>

        <section aria-label="Statistic selector" className="flex flex-col items-start gap-4">
          <StatisticSwitch id="profit" label="Profit" />
          <StatisticSwitch id="annualized_return" label="Annualized Return" />
          <StatisticSwitch id="percent_return" label="Percent Return" />
        </section>
      </form>
    </main>
  )
}


interface StatisticSwitchProps {
  id: string
  label: string
}
const StatisticSwitch = ({ id, label }: StatisticSwitchProps) => {
  return (
    <div className="flex items-center space-x-2">
    <Switch id={id} />
    <Label htmlFor={id}>{label}</Label>
  </div>
  )
}
