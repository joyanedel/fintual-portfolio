"use client"

import { useState } from "react"
import { sub, subDays } from "date-fns"
import { DateRange } from "react-day-picker"

import { Calendar } from "@/components/ui/calendar"
import { Switch } from "@/components/ui/switch"
import { Form, FormControl, FormField, FormItem, FormLabel } from "@/components/ui/form"

import { z } from "zod"
import { zodResolver } from "@hookform/resolvers/zod"
import { useForm, UseFormReturn } from "react-hook-form"
import { Button } from "@/components/ui/button"
import { statisticFormSchema } from "@/lib/types"
import useStatistics, { StatisticsResult } from "@/hooks/useStatistics"
import { ClientProviders } from "./providers"

export default function Home() {
  const [date, setDate] = useState<DateRange | undefined>({
    from: subDays(new Date(), 30),
    to: new Date(),
  })
  const {handleSubmit, statisticsResult, isFetching} = useStatistics()

  const statisticsForm = useForm<z.infer<typeof statisticFormSchema>>({
    resolver: zodResolver(statisticFormSchema),
    defaultValues: {
      profit: true,
    }
  })

  function onSubmit(data: z.infer<typeof statisticFormSchema>) {
    console.log(data)
    handleSubmit({
      start_date: date?.from || new Date(),
      end_date: date?.to || new Date(),
      profit: data.profit,
      annualized_return: data.annualized_return,
      percent_return: data.percent_return
    })
  }

  return (
    <ClientProviders>
      <main className="flex-col w-full">
        <header className="pb-4">
          <h1 className="text-center text-3xl">Welcome to Fintual Portfolio Sandbox</h1>
          <h6 className="text-center">Here you will be able to calculate the profit within a time period, annualized return and percent return</h6>
        </header>

        <StatisticForm statisticsForm={statisticsForm} onSubmit={onSubmit} date={date} setDate={setDate} />

        {isFetching && <p>Loading...</p>}
        {statisticsResult && <StatisticResult statisticsResult={statisticsResult} />}
      </main>
    </ClientProviders>
  )
}

interface StatisticFormProps {
  onSubmit: (data: z.infer<typeof statisticFormSchema>) => void
  statisticsForm: UseFormReturn<z.infer<typeof statisticFormSchema>>

  date: DateRange | undefined
  setDate: (date: DateRange | undefined) => void
}
const StatisticForm = ({statisticsForm, onSubmit, date, setDate}: StatisticFormProps) => (
  <Form {...statisticsForm}>
  <form onSubmit={statisticsForm.handleSubmit(onSubmit)} className="flex flex-col justify-start items-center">
    <div className="flex justify-evenly items-start gap-16 py-8">
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

      <section aria-label="Statistic selector" className="flex flex-col items-start gap-4 pt-4">
        <FormField
          control={statisticsForm.control}
          name="profit"
          render={({field}) => <StatisticSwitch id="profit" label="Profit" value={field.value} onChange={field.onChange} />}
        />
        <FormField
          control={statisticsForm.control}
          name="annualized_return"
          render={({field}) => <StatisticSwitch id="annualized_return" label="Annualized Return" value={field.value} onChange={field.onChange} />}
        />
        <FormField
          control={statisticsForm.control}
          name="percent_return"
          render={({field}) => <StatisticSwitch id="percent_return" label="Percent Return" value={field.value} onChange={field.onChange} />}
        />
      </section>
    </div>


    <Button type="submit">
      Calculate
    </Button>
  </form>
</Form>
)

interface StatisticSwitchProps {
  id: string
  label: string,
  value: boolean,
  onChange: (value: boolean) => void
}
const StatisticSwitch = ({ id, label, onChange, value }: StatisticSwitchProps) => {
  return (
      <FormItem className="flex items-center justify-center space-x-2">
        <FormControl>
          <Switch id={id} checked={value} onCheckedChange={onChange} />
        </FormControl>
        <FormLabel htmlFor={id}>{label}</FormLabel>
      </FormItem>
  )
}

interface StatisticResultProps {
  statisticsResult: StatisticsResult | null
}
const StatisticResult = ({statisticsResult}: StatisticResultProps) => {
  console.log(statisticsResult)
  return (
    <section aria-label="Statistics result" className="flex flex-col items-start gap-4 pt-4">
      <h2 className="text-2xl">Statistics Result</h2>
      <ul className="flex flex-col gap-4">
        {statisticsResult?.profit && <li>Profit: {statisticsResult.profit}</li>}
        {statisticsResult?.annualized_return && <li>Annualized Return: {statisticsResult.annualized_return}</li>}
        {statisticsResult?.percent_return && <li>Percent Return: {statisticsResult.percent_return}</li>}
      </ul>
    </section>
  )
}
