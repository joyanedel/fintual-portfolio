import { z } from "zod"

export const statisticFormSchema = z.object({
  profit: z.boolean().default(true),
  annualized_return: z.boolean(),
  percent_return: z.boolean(),
})
